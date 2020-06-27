/**
* In plantuml the condition of the first if is also used for nested if.
* -> ifbeginlineNestedArray_method() used wrong array for node.
*/

int x, y;

int main()
{
    if(x == 1)
    {
        //$ action 1
        
        if(y < 6)
        {
            //$ action 2
        }
        else if(y < 10)
        {
            //$ action 3
        }
    }
}
