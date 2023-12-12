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
$name=$_POST["n"];
$des=$_POST["Des"];
$dep=$_POST["Dep"];
$date=$_POST["Da"];
$sql = "INSERT INTO Airline (Name, Destination,Departure,date)
VALUES ('$name','$des','$dep','$date')";
if ($conn->query($sql) === TRUE) {
  echo "Booking Successfully";
} else {
  echo "Error: " . $sql . "<br>" . $conn->error;
}
$conn->close();
}
?>
<html>
<head>
<meta charset="UFT-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
</head>
<body>
<div>
<img src="/home/mbits/Desktop/apple.jpg" height=50 width=50>
</div>
<h2>Airline Ticket Booking</h2>
<form method="post">
	
	Name:<input type="text" name="n" required><br><br>
	Destination:<input type="text" name="Des" required><br><br>
	Departure(FN/AN):<input type="text" name="Dep"required><br><br>
        Date:<input type="date" name="Da"required><br><br>
        <input type="submit"  value="press here for booking" id="submit" required>
</form>
</body>
</html>

