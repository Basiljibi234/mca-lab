<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "basil_db";
$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

if($_POST){
$name=$_POST["name"];
$email=$_POST["email"];
$course=$_POST["course"];

$sql = "INSERT INTO reg (name,email,course) VALUES ('$name', '$email', '$course')";

if ($conn->query($sql) === TRUE) {
  echo "New record created successfully";
} else {
  echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
}
?>
<html>
<head></head>
<body> 
<form method="post">
  <div class="container">
    <h1>Register</h1>
    <hr>
    <label for="name"><b>Name</b></label>
    <input type="text" placeholder="Enter Name" name="name" id="name" required>
    <label for="email"><b>Email</b></label>
    <input type="text" placeholder="Enter Email" name="email" id="email" required>
    <label for="course"><b>course</b></label>
    <input type="text" placeholder="Enter course" name="course" id="course" required>
    </hr>
    <input type="submit"  name="submit" id="submit" required>
  </div>
</form>
</body>
</html> 
