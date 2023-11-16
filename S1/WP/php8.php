<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UFT-8">
	<meta name="viewport" content="width=device-width,initial-scale=1.0">
	<title>database</title>
	<style>
table
{
width:50%;
border-collapse:collapse;
margin:20px0;
}
table,th,td{
border:1px soild black;
}
th,td{
padding:10px;
text-align:left;
}
</style>
</head>
<body>
<?php
$servername="localhost";
$username="root";
$password="";
$database="basil_db";
$conn=new mysqli($servername,$username,$password,$database);
if($conn->connect_error){
die("connection failed:".$conn->connect_error);
}
$sql="select*from student";
$result=$conn->query($sql);
if($result->num_rows>0)
{
echo"<table><tr><th>Roll_no</th><th>Name</th><th>Age</th><th>place</th></tr>";
while($row=$result->fetch_assoc()){
echo"<tr><td>".$row["rollno"]."</td><td>".$row["name"]."</td><td>".$row["age"]."</td><td>".$row["place"]."</td></tr>";
}
echo"</table>";
}
else{
echo"0 results found";
}
$conn->close();
?>
</body>
</html>
