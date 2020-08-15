<?
/**
 * Database.php
 *
 * The Database class is meant to simplify the task of accessing
 * information from the website's database.
 *
 * Rewritten for PSQL and modified by: Pavel Dorovskoy
 * Written by: Jpmaster77 a.k.a. The Grandmaster of C++ (GMC)
 */
require_once "config.inc";
require_once 'ActiveRecord.php';
require_once '/usr/share/pear/Log.php';

ActiveRecord\Config::initialize(function($cfg)
{
    $cfg->set_model_directory(__DIR__.'/models/');
    $cfg->set_connections(array(
        'development' => 'pgsql://rsadmin:b1u3b1rd@localhost/remotesensing'));
        //'development' => 'pgsql:host=dbname='.DB_NAME." user=".DB_USER." password=".DB_PASS));
        //'development' => 'pgsql:host=localhost;port=5432;dbname=remotesensing;user=rsadmin;password=b1u3b1rd'));
    $logger = Log::singleton('file','/tmp/phpar.log','ident',array('mode' => 0664, 'timeFormat' =>  '%Y-%m-%d %H:%M:%S'));
  
    $cfg->set_logging(true);
    $cfg->set_logger($logger);
});

class PostgreSQLDB
{
	protected $connection;         //The PSQL database connection
	public $num_active_users;   //Number of active users viewing site
	public $num_active_guests;  //Number of active guests viewing site
	public $num_members;        //Number of signed-up users
	public $debug;
	/* Note: call getNumMembers() to access $num_members! */

	/* Class constructor */
	function PostgreSQLDB(){
		/* Make connection to database */
		if(DB_LOCAL)
			$str = "dbname=".DB_NAME." user=".DB_USER." password=".DB_PASS;
		else
			$str = "host=".DB_SERVER." dbname=".DB_NAME." user=".DB_USER." password=".DB_PASS;

		$this->connection = pg_connect($str)
		or die('Could not connect: ' . pg_last_error());

		/**
       * Only query database to find out number of members
       * when getNumMembers() is called for the first time,
       * until then, default value set.
       */
		$this->num_members = -1;

		if(TRACK_VISITORS){
			/* Calculate number of users at site */
			$this->calcNumActiveUsers();

			/* Calculate number of guests at site */
			$this->calcNumActiveGuests();
		}
	}

	/**
    * confirmUserPass - Checks whether or not the given
    * username is in the database, if so it checks if the
    * given password is the same password in the database
    * for that user. If the user doesn't exist or if the
    * passwords don't match up, it returns an error code
    * (1 or 2). On success it returns 0.
    */
	function confirmUserPass($username, $password){
		/* Add slashes if necessary (for query) */
		if(!get_magic_quotes_gpc()) {
			$username = addslashes($username);
		}

		/* Verify that user is in database */
		$q = "SELECT password FROM ".TBL_USERS." WHERE username = '$username'";
		$result = pg_query($this->connection, $q);

		if(!$result || (pg_num_rows($result) < 1)){
			return 1; //Indicates username failure
		}

		/* Retrieve password from result, strip slashes */
		$dbarray = pg_fetch_array($result);
		$dbarray['password'] = stripslashes($dbarray['password']);
		$password = stripslashes($password);

		/* Validate that password is correct */
		if($password == $dbarray['password']){
			return 0; //Success! Username and password confirmed
		}
		else{
			return 2; //Indicates password failure
		}
	}

	/**
    * confirmSessID - Checks whether or not the given
    * username is in the database, if so it checks if the
    * given sessid is the same sessid in the database
    * for that user. If the user doesn't exist or if the
    * sessids don't match up, it returns an error code
    * (1 or 2). On success it returns 0.
    */
	function confirmSessID($username, $sessid){
		/* Add slashes if necessary (for query) */
		if(!get_magic_quotes_gpc()) {
			$username = addslashes($username);
		}

		/* Verify that user is in database */
		$q = "SELECT sessid FROM ".TBL_USERS." WHERE username = '$username'";
		$result = pg_query($this->connection, $q);
		if(!$result || (pg_num_rows($result) < 1)){
			return 1; //Indicates username failure
		}

		/* Retrieve sessid from result, strip slashes */
		$dbarray = pg_fetch_array($result);
		$dbarray['sessid'] = stripslashes($dbarray['sessid']);
		$sessid = stripslashes($sessid);

		/* Validate that sessid is correct */
		if($sessid == $dbarray['sessid']){
			return 0; //Success! Username and sessid confirmed
		}
		else{
			return 2; //Indicates sessid invalid
		}
	}

	/**
    * usernameTaken - Returns true if the username has
    * been taken by another user, false otherwise.
    */
	function usernameTaken($username){
		if(!get_magic_quotes_gpc()){
			$username = addslashes($username);
		}
		$q = "SELECT username FROM ".TBL_USERS." WHERE username = '$username'";
		$result = pg_query($this->connection, $q);
		return (pg_num_rows($result) > 0);
	}

	/**
    * usernameBanned - Returns true if the username has
    * been banned by the administrator.
    */
	function usernameBanned($username){
		if(!get_magic_quotes_gpc()){
			$username = addslashes($username);
		}
		$q = "SELECT username FROM ".TBL_BANNED_USERS." WHERE username = '$username'";
		$result = pg_query($this->connection, $q);
		return (pg_num_rows($result) > 0);
	}


    function emailTaken($username){
        if(!get_magic_quotes_gpc()){
            $username = addslashes($username);
        }
        $q = "SELECT email FROM ".TBL_USERS." WHERE email = '$username'";
        $result = pg_query($this->connection, $q);
        return (pg_num_rows($result) > 0);
    }


	/**
    * addNewUser - Inserts the given (username, password, email)
    * info into the database. Appropriate user level is set.
    * Returns true on success, false otherwise.
    */
	function addNewUser($username, $password, $email){
		/* If admin sign up, give admin user level */
		if(strcasecmp($username, ADMIN_NAME) == 0){
			$ulevel = ADMIN_LEVEL;
		}else{
			$ulevel = USER_LEVEL;
		}
		$q = "INSERT INTO ".TBL_USERS.
		" (username, password, email, level, createdate, roleid  )".
		" VALUES ('$username', '$password', '$email', $ulevel, NOW(), 0)";
		if (pg_query($this->connection, $q)){
			return true;
		}else{
			echo $q;
			//echo '<br>test<br>';
			return false;
		}
	}

	/**
    * updateUserField - Updates a field, specified by the field
    * parameter, in the user's row of the database.
    */
	function updateUserField($username, $field, $value){
		$q = "UPDATE ".TBL_USERS." SET ".$field." = '$value' WHERE username = '$username'";
		return pg_query($this->connection, $q);
	}

	/**
    * updateField - Updates a field, specified by the field
    * parameter, in the user's row of the database.
    */
	function updatePhotoField($photoid, $field, $value){
		//Checking for point is hackish, 
		//but the goal is to not escape PostGIS function which are strings
		if (is_numeric($value) or $field == 'point'){
			$q = "UPDATE photos SET ".$field." = $value WHERE id = '$photoid'";
		}else{
			$q = "UPDATE photos SET ".$field." = '$value' WHERE id = '$photoid'";
		}
		if ($this->debug) error_log($q);
		return pg_query($this->connection, $q);
	}

	/**
    * getUserInfo - Returns the result array from a mysql
    * query asking for all information stored regarding
    * the given username. If query fails, NULL is returned.
    */
	function getUserInfo($username){
		$q = "SELECT * FROM ".TBL_USERS." WHERE username = '$username'";
		$result = pg_query($this->connection, $q);
		/* Error occurred, return given name by default */
		if(!$result || (pg_num_rows($result) < 1)){
			return NULL;
		}
		/* Return result array */
		$dbarray = pg_fetch_array($result);
		return $dbarray;
	}

	function getUserInfoById($id){
		$q = "SELECT * FROM ".TBL_USERS." WHERE id = $id";
		$result = pg_query($this->connection, $q);
		/* Error occurred, return given name by default */
		if(!$result || (pg_num_rows($result) < 1)){
			return NULL;
		}
		/* Return result array */
		$dbarray = pg_fetch_array($result);
		return $dbarray;
	}

    function getUserByEmail($email){
        $q = "SELECT username FROM users WHERE email = '".pg_escape_string($email)."'";
        $result = pg_query($this->connection, $q);
        $arr = pg_fetch_array($result);
        return $arr['username'];
    }

	/**
    * getNumMembers - Returns the number of signed-up users
    * of the website, banned members not included. The first
    * time the function is called on page load, the database
    * is queried, on subsequent calls, the stored result
    * is returned. This is to improve efficiency, effectively
    * not querying the database when no call is made.
    */
	function getNumMembers(){
		if($this->num_members < 0){
			$q = "SELECT * FROM ".TBL_USERS;
			$result = pg_query($this->connection, $q);
			$this->num_members = pg_num_rows($result);
		}
		return $this->num_members;
	}

	/**
    * getSequenceID - Returns id of the last added item for
    * any table. Depends on use of autoincrement 'id' field.
    */
	function getSequenceID($table){
		$q = "SELECT nextval('".$table."_id_seq') AS id;";
		$result = pg_query($this->connection, $q);
		$arr = pg_fetch_array($result);
		return $arr['id'];
	}

	/**
    * calcNumActiveUsers - Finds out how many active users
    * are viewing site and sets class variable accordingly.
    */
	function calcNumActiveUsers(){
		/* Calculate number of users at site */
		$q = "SELECT * FROM ".TBL_ACTIVE_USERS;
		$result = pg_query($this->connection, $q);
		$this->num_active_users = pg_num_rows($result);
	}

	/**
    * calcNumActiveGuests - Finds out how many active guests
    * are viewing site and sets class variable accordingly.
    */
	function calcNumActiveGuests(){
		/* Calculate number of guests at site */
		$q = "SELECT * FROM ".TBL_ACTIVE_GUESTS;
		$result = pg_query($this->connection, $q);
		$this->num_active_guests = pg_num_rows($result);
	}

	/**
    * addActiveUser - Updates username's last active timestamp
    * in the database, and also adds him to the table of
    * active users, or updates timestamp if already there.
    */
	function addActiveUser($username, $time){
		$q = "UPDATE ".TBL_USERS." SET timestamp = '$time' WHERE username = '$username'";
		pg_query($this->connection, $q);

		if(!TRACK_VISITORS) return;
		$q = "REPLACE INTO ".TBL_ACTIVE_USERS." VALUES ('$username', '$time')";
		pg_query($this->connection, $q);
		$this->calcNumActiveUsers();
	}

	/* addActiveGuest - Adds guest to active guests table */
	function addActiveGuest($ip, $time){
		if(!TRACK_VISITORS) return;
		$q = "REPLACE INTO ".TBL_ACTIVE_GUESTS." VALUES ('$ip', '$time')";
		pg_query($this->connection, $q);
		$this->calcNumActiveGuests();
	}

	/* These functions are self explanatory, no need for comments */

	/* removeActiveUser */
	function removeActiveUser($username){
		if(!TRACK_VISITORS) return;
		$q = "DELETE FROM ".TBL_ACTIVE_USERS." WHERE username = '$username'";
		pg_query($this->connection, $q);
		$this->calcNumActiveUsers();
	}

	/* removeActiveGuest */
	function removeActiveGuest($ip){
		if(!TRACK_VISITORS) return;
		$q = "DELETE FROM ".TBL_ACTIVE_GUESTS." WHERE ip = '$ip'";
		pg_query($this->connection, $q);
		$this->calcNumActiveGuests();
	}

	/* removeInactiveUsers */
	function removeInactiveUsers(){
		if(!TRACK_VISITORS) return;
		$timeout = time()-USER_TIMEOUT*60;
		$q = "DELETE FROM ".TBL_ACTIVE_USERS." WHERE timestamp < $timeout";
		pg_query($this->connection, $q);
		$this->calcNumActiveUsers();
	}

	/* removeInactiveGuests */
	function removeInactiveGuests(){
		if(!TRACK_VISITORS) return;
		$timeout = time()-GUEST_TIMEOUT*60;
		$q = "DELETE FROM ".TBL_ACTIVE_GUESTS." WHERE timestamp < $timeout";
		pg_query($this->connection, $q);
		$this->calcNumActiveGuests();
	}

	//function

	/**
    * query - Performs the given query on the database and
    * returns the result, which may be false, true or a
    * resource identifier.
    */
	function query($query){
		//error_log($query);
		return pg_query($this->connection,$query);
	}

	function queryFetch($query){
		return pg_fetch_all(pg_query($this->connection,$query));
	}

	function lastError(){
		echo pg_last_error($this->connection);
	}

	function printTable($table){
		$query = "select * FROM ".$table;
		$result = pg_query($this->connection,$query) or die('Query failed: ' . pg_last_error());

		// Printing results in HTML
		echo "<table>\n";
		while ($line = pg_fetch_array($result, null, PGSQL_ASSOC)) {
			echo "\t<tr>\n";
			foreach ($line as $col_value) {
				echo "\t\t<td>$col_value</td>\n";
			}
			echo "\t</tr>\n";
		}
		echo "</table>\n";
	}

	function printResult($result){
		// Printing results in HTML
		echo "<pre>";
		echo "<table border=\"1\">\n";
		while ($line = pg_fetch_array($result, null, PGSQL_ASSOC)) {
			echo "\t<tr>\n";
			foreach ($line as $col_value) {
				echo "\t\t<td>$col_value</td>\n";
			}
			echo "\t</tr>\n";
		}
		echo "</table>\n</pre>";
	}

	/**   Takes a result set and turns the optional column into
	 *   an array
	 */
	function resultColumnToArray($result, $col=0) {
		$rows=pg_numrows($result);
		for ($i=0; $i<$rows; $i++) {
			$array[]=pg_fetch_result($result,$i,$col);
		}
		return $array;
	}

};

/* Create database connection */
$database = new PostgreSQLDB;

?>