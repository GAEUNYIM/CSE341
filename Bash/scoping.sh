x=50
y=100


function foo() {
    echo "In foo: y = $y" # $y: access to the value of variable y
}

function bar() {
    y=$1 # $1: acces to the actual paramter
    echo "In bar: x = $x"
    echo "In bar: y = $y"
    baz $((y+1))
}

# Let's define one more function
function baz() {
    y=$1 # $1: acces to the actual paramter
    echo "In baz: x = $x"
    echo "In baz: y = $y"
    foo
}

bar 1
