#include <wiringPi.h>
#include <stdio.h>
#define LED_PIN 7

int main (void)
{
    wiringPiSetup ();
    pinMode (LED_PIN, OUTPUT);
    int a=0;
    int b=0;
    printf("1=불 키기 2=불 끄기 3=프로그램 종료");
        while (b==0)
    {
        scanf("%d",&a);
        if (a==1){
            digitalWrite (LED_PIN, HIGH);
        }
        if (a==0){
            digitalWrite (LED_PIN,  LOW);
        }
        if (a==3){
            break;
        }
    }
    printf("끝");
    return 0;
}