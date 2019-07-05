<?php
$conn = new mysqli('localhost', 'chicktech', 'chicktech', 'chicktech_test');
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
$sql = "select name from people WHERE name LIKE 'b%' AND age<11";
$result = $conn->query($sql);
while($row = $result->fetch_assoc()) {
echo $row["name"]. "<br>"; 
}
$conn->close();
?>
