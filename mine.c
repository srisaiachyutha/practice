#include<stdio.h>
#include<stdlib.h>


int count=100;
void display(char m[10][10],int m1[10][10]){
int i,j;
printf("\n");
for(i=1;i<10;i++)
printf("  %d  ",i);
printf("\n");
for(i=0;i<10;i++){
printf("  %d  ",i);
for(j=0;j<10;j++){
if(m1[i][j]==1)
printf("  %c  ",m[i][j]);
else
printf("      ");
}printf("\n\n");}

}



void create(char m[10][10]){
int x,y,i,j,c;

for(i=0;i<10;i++){
	for(j=0;j<10;j++){c=0;
if(m[i][j]!='b'){
	x=i-1;y=j-1;
	if(x>=0&&y>=0&&x<10&&y<10&&m[x][y]=='b')c++;
x=i-1;y=j;
	if(x>=0&&y>=0&&x<10&&y<10&&m[x][y]=='b')c++;

x=i-1;y=j+1;
	if(x>=0&&y>=0&&x<10&&y<10&&m[x][y]=='b')c++;

x=i;y=j-1;
	if(x>=0&&y>=0&&x<10&&y<10&&m[x][y]=='b')c++;

x=i;y=j+1;
	if(x>=0&&y>=0&&x<10&&y<10&&m[x][y]=='b')c++;

x=i+1;y=j-1;
	if(x>=0&&y>=0&&x<10&&y<10&&m[x][y]=='b')c++;

x=i+1;y=j;
	if(x>=0&&y>=0&&x<10&&y<10&&m[x][y]=='b')c++;

x=i+1;y=j+1;
	if(x>=0&&y>=0&&x<10&&y<10&&m[x][y]=='b')c++;

m[i][j]=c+'0';
			}
		}
	}
}


void start(char m[10][10],int m1[10][10],int x1,int y1){
int i,j,k,x,y;
m1[x1][y1]=1;count--;


if(m[x1][y1]=='_')
m[x1][y1]=' ';

x=x1-1;y=y1-1;
if(x>=0&&y>=0&&x<10&&y<10&&m[x][y]=='_')
	start(m,m1,x,y);

x=x1-1;y=y1;
if(x>=0&&y>=0&&x<10&&y<10&&m[x][y]=='_')
	start(m,m1,x,y);

x=x1-1;y=y1+1;
if(x>=0&&y>=0&&x<10&&y<10&&m[x][y]=='_')
	start(m,m1,x,y);

x=x1;y=y1-1;
if(x>=0&&y>=0&&x<10&&y<10&&m[x][y]=='_')
	start(m,m1,x,y);

x=x1;y=y1+1;
if(x>=0&&y>=0&&x<10&&y<10&&m[x][y]=='_')
	start(m,m1,x,y);

x=x1+1;y=y1-1;
if(x>=0&&y>=0&&x<10&&y<10&&m[x][y]=='_')
	start(m,m1,x,y);

x=x1+1;y=y1;
if(x>=0&&y>=0&&x<10&&y<10&&m[x][y]=='_')
	start(m,m1,x,y);

x=x1+1;y=y1+1;
if(x>=0&&y>=0&&x<10&&y<10&&m[x][y]=='_')
	start(m,m1,x,y);


}


int main()
{
 char ma[10][10];
int x,y,cx,cy,win=0;
 int m[10][10],i,j,k,v,c=10;
for(i=0;i<10;i++)
	for(j=0;j<10;j++){
	ma[i][j]='_';
	m[i][j]=0;
	}

while(c>0){
x=rand()%10;
y=rand()%10;
ma[x][y]='b';
c--;
}


create(ma);


while(count>90){
printf("enter the x and y coordinates\n");
scanf("%d%d",&cx,&cy);
if(ma[cx][cy]=='b'){break;win=0;}
start(ma,m,cx,cy);
display(ma,m);
}


if(win==0)
printf("you have lost the game");
else printf("you have won the game");


return 0;
}