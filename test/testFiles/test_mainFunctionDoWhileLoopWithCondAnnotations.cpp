/**
 * Show while loop and annotated condition in plantuml.
 * - a loop and the conditon is shown if variable is declared, but its a while loop.
 *
 * Generated plantuml contains while loop and no do-while loop.
 * --> added different handling of conditional annotation for do loop
*/

int x;

int main()
{
    //$ [condition 1]
    do
    {
        //$ action 1
    } while(x != 1);
}
