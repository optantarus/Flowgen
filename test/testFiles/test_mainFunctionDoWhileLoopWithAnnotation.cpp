// Generated plantum contains only action without loop structure
//   Check if loop structure should not be shown if it has no annotation (an if structure in such a case is shown without condition)
//   - should be shown, declaration of variables fixes this problem
//
// TODO: Last character of condition is mising in generated plantuml.

int x, b;

int main()
{
    do
    {
        //$ action 1
    } while(x < b);
}
