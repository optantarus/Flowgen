/**
* Generated plantuml contains if structure with no condition:
*   Check if if without annotation should be shown (for loops there is different behavior, they are not shown):
*   - it should be shown
*   - it is nessesary to delare the variables in the condition to get it in the AST
*
* Last character of condition is missing.
* - fixed in code: removed string_condition = string_condition[:-1]
*/

int x;

int main()
{
    if(x == 1)
    {
        //$ action 1
    }
}
