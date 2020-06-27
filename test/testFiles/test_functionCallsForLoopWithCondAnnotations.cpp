/**
* main function not reconized by build_db ?
* -> is current implementation, needs explicit action annotation
*/

void call_do(void);

int main()
{
    //$ [condition 1]
    for(int i=0; i<6; i++)
    {
        //$ call do
        call_do() //$
    }
}

void call_do()
{
    //$ action 2
}
