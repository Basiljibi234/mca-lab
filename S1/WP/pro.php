<?php
$name=$_GET["name"];
echo "hello",$name;

?>
<html>
<body>
<form>
	name:<input type="text"name="name">
	Name:<input type="text"name="name" value=<%=$name>/>
	
</form>
</body>
</html>
