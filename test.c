int main() {
    /*a*/
    int a;
    float b;
    int c;
    float e = 1e1;
    char c = 'a'; 
    c = '\n';
    char* s = "hello";
    c=10;
    if(a<=b||a==b) {
        a = 1 + 10;
        b = 10.9 + 8.9;
    }
    b = 1.11 * 8.9;
    while(a) {
        b = 10.44;
        e = 990.45;
        c = 90;
    }
    c = 80;
}

int func1 () {
}
/*errorzone*/
"abc; /*string*/
'a; /*char*/
1e-; /*const*/
/*error /*notes*/