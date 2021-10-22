```php
// syntax
<?php
    echo "Thiis same Print in Python<br>";
    echo "; is esentail"
    // 한줄주석
    /* 여러 줄 
    주석*/
?>
```

```php
// 변수
$txt = "Hello"

$x = 10;
$y = 5;
echo = $x +$y
```

```php
<?php
echo "<h2>PHP is Fun!</h2>";
echo "Hello world!<br>";
echo "I'm about to learn PHP!<br>";
echo "This ", "string ", "was ", "made ", "with multiple parameters.";
?>
    
<?php
print "<h2>PHP is Fun!</h2>";
print "Hello world!<br>";
print "I'm about to learn PHP!";
?>
```

## PHP Data Types

Variables can store data of different types, and different data types can do different things.

PHP supports the following data types:

- String
- Integer
- Float (floating point numbers - also called double)
- Boolean
- Array
- Object
- NULL
- Resource

```php
<?php
$x = "Hello world!";
$y = 'Hello world!';

echo $x;
echo "<br>";
echo $y;
?>
```

## PHP Integer

An integer data type is a non-decimal number between -2,147,483,648 and 2,147,483,647.

Rules for integers:

- An integer must have at least one digit
- An integer must not have a decimal point
- An integer can be either positive or negative
- Integers can be specified in: decimal (base 10), hexadecimal (base 16), octal (base 8), or binary (base 2) notation

In the following example $x is an integer. The PHP var_dump() function returns the data type and value:

```php
//integer
<?php  
$x = 5985;
echo "$x<br>";
var_dump($x)
?> 

/* 
결과
5985
int(5985)
*/

//float
<?php  
$x = 10.365;
echo "$x<br>";
var_dump($x);
?>  
    
/*
결과
<?php  
10.365
float(10.365)
?>  
*/
```

## PHP Boolean

A Boolean represents two possible states: TRUE or FALSE.

$x = true;
$y = false;

Booleans are often used in conditional testing. You will learn more about conditional testing in a later chapter of this tutorial.

------

## PHP Array

An array stores multiple values in one single variable.

In the following example $cars is an array. The PHP var_dump() function returns the data type and value:

```php
<?php  
$cars = array("Volvo","BMW","Toyota");
var_dump($cars);
?>  

/*
array(3) { [0]=> string(5) "Volvo" [1]=> string(3) "BMW" [2]=> string(6) "Toyota" }
*/
```

## PHP Object

Classes and objects are the two main aspects of object-oriented programming.

클래스와 객체는 객체 지향 프로그래밍의 두 가지 주요 측면입니다.

A class is a template for objects, and an object is an instance of a class.

When the individual objects are created, they inherit all the properties and behaviors from the class, but each object will have different values for the properties.

Let's assume we have a class named Car. A Car can have properties like model, color, etc. We can define variables like $model, $color, and so on, to hold the values of these properties.

Car라는 클래스가 있다고 가정해 봅시다. Car는 모델, 색상 등과 같은 속성을 가질 수 있습니다. 이러한 속성의 값을 유지하기 위해 $model, $color 등과 같은 변수를 정의할 수 있습니다.

When the individual objects (Volvo, BMW, Toyota, etc.) are created, they inherit all the properties and behaviors from the class, but each object will have different values for the properties.

개별 개체(Volvo, BMW, Toyota 등)가 생성되면 클래스에서 모든 속성과 동작을 상속하지만 각 개체는 속성에 대해 서로 다른 값을 갖습니다.

If you create a __construct() function, PHP will automatically call this function when you create an object from a class.

__construct() 함수를 생성하면 클래스에서 객체를 생성할 때 PHP가 자동으로 이 함수를 호출합니다.

```php
<?php
class Car {
  //class Car(color,model)""
  public $color;
  public $model;
  public function __construct($color, $model) {
    //_construct($color, $model) == __init__(color,model):
    $this->color = $color; //self.color = color
    $this->model = $model; //self.model = model
  }
  /*def message():
  return "My car is a", color, model,"!"
  */
  public function message() {
    return "My car is a " . $this->color . " " . $this->model . "!";
  }
}

$myCar = new Car("black", "Volvo");
echo $myCar -> message();
echo "<br>";
$myCar = new Car("red", "Toyota");
echo $myCar -> message();
?>

/*
My car is a white Volvo!
My car is a red Toyota!
*/
```

## PHP String Functions

In this chapter we will look at some commonly used functions to manipulate strings.

------

## strlen() - Return the Length of a String

The PHP `strlen()` function returns the length of a string.

str + len

```php
<?php
    echo strlen("Hello world"); //output 12
?>
```

## str_word_count() - Count Words in a String

The PHP `str_word_count()` function counts the number of words in a string.

```php
<?php
    
    ehco str_word_count("Hello world"); //output 2 단어 수 카운트
?>
```



## strrev() - Reverse a String

The PHP `strrev()` function reverses a string.

```php
// 문자 뒤집기
<?php
    echo strrev("Hello world"); // dlrow olleH
?>
```



## strpos() - Search For a Text Within a String

The PHP `strpos()` function searches for a specific text within a string. If a match is found, the function returns the character position of the first match. If no match is found, it will return FALSE.

```php
<?php
    echo strpos("Hello world","world"); //6
?>
```



## str_replace() - Replace Text Within a String

The PHP `str_replace()` function replaces some characters with some other characters in a string.

```php
<?php
    echo str_replace("world",'Dolly',"Hello world1"); // Hello Dolly!
?>
```

### 형변환

```php
<?php
// Cast float -> int 
$x = 23465.768;
$int_cast = (int)$x;
echo $int_cast;
  
echo "<br>";

// Cast string -> int
$x = "23465.768";
$int_cast = (int)$x;
echo $int_cast;
?> 
```

## Create a PHP Constant

To create a constant, use the `define()` function.

### Syntax

define(*name*, *value*, *case-insensitive*)

Parameters:

- *name*: Specifies the name of the constant

- *value*: Specifies the value of the constant

- *case-insensitive*: Specifies whether the constant name should be case-insensitive. Default is false (대소문자구분여부 false = 구분한다.)

  

```php
<?php
// define("key","value",case-insensitive)
define("GREETING", "Welcome to W3Schools.com!");
echo GREETING;
?>
```

## The PHP switch Statement

Use the `switch` statement to **select one of many blocks of code to be executed**.

### Syntax

```php
<?php
$favcolor = "red";

switch ($favcolor) {
  case "red":
    echo "Your favorite color is red!";
    break;
  case "blue":
    echo "Your favorite color is blue!";
    break;
  case "green":
    echo "Your favorite color is green!";
    break;
  default:
    echo "Your favorite color is neither red, blue, nor green!";
}
?>
```

This is how it works: First we have a single expression *n* (most often a variable), that is evaluated once. The value of the expression is then compared with the values for each case in the structure. If there is a match, the block of code associated with that case is executed. Use `break` to prevent the code from running into the next case automatically. The `default` statement is used if no match is found.



In the following chapters you will learn how to repeat code by using loops in PHP.

------

## PHP Loops

Often when you write code, you want the same block of code to run over and over again a certain number of times. So, instead of adding several almost equal code-lines in a script, we can use loops.

Loops are used to execute the same block of code again and again, as long as a certain condition is true.

In PHP, we have the following loop types:

- `while` - loops through a block of code as long as the specified condition is true
- `do...while` - loops through a block of code once, and then repeats the loop as long as the specified condition is true
- `for` - loops through a block of code a specified number of times
- `foreach` - loops through a block of code for each element in an array

The following chapters will explain and give examples of each loop type.

```php
<?php
$x = 1;

do { //명령
  echo "The number is: $x <br>";
  $x++;
} while ($x <= 5); //조건
?>
```

```php
// for loop

<?php
for ($x = 0; $x <= 10; $x++) {
  echo "The number is: $x <br>";
}
?>
```

```php
<?php
$colors = array("red", "green", "blue", "yellow");

foreach ($colors as $value) {
  echo "$value <br>";
}
?>
```

## PHP Return Type Declarations

PHP 7 also supports Type Declarations for the `return` statement. Like with the type declaration for function arguments, by enabling the strict requirement, it will throw a "Fatal Error" on a type mismatch.

To declare a type for the function return, add a colon ( `:` ) and the type right before the opening curly ( `{` )bracket when declaring the function.

In the following example we specify the return type for the function:

```php
<?php declare(strict_types=1); // strict requirement
function addNumbers(float $a, float $b) : float {
  return $a + $b;
}
echo addNumbers(1.2, 5.2);
?> // 6.4

<?php declare(strict_types=1); // strict requirement
function addNumbers(float $a, float $b) : int {
  return (int)($a + $b);
}
echo addNumbers(1.2, 5.2);
?> //6

```

```php
/*
기본적으로 복사한 값을 사용하나 
`&`를 사용하면 return이 없더라도 더하기 가능
*/

<?php
function add_five(&$value) {
  $value += 5;
}

$num = 2;
add_five($num);
echo $num;
?> //7

<?php
function add_five($value) {
  $value += 5;
}

$num = 2;
add_five($num);
echo $num;
?> //2

```

