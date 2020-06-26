/**
* call_2() is intentionally not declared. It should not be a link from main shown in generated plantuml.
* 
* TODO: main function not in flowdb ? Not generated in plantuml.
*/

int x;

void call_1(void);

int main()
{
    //$ [condition 1]
    if(x == 1)
    {
        call_1() //$
    }
    //$ [condition 2]
    else
    {
        call_2() //$
    }
}


void call_1()
{
    //$ action 1
}

void call_2()
{
    //$ action 2
}
