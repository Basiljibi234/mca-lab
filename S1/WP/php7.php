<?php
$db=new mysqli("localhost","root","","basil_db");
if($db->connect_error)
{
die("connection failed:".$db->connect_error);
}
$result=$db->query("select*from student");
while($row=$result->fetch_assoc())
{
echo"name:".$row['name']."<br>";
}
$db->close();
?>
