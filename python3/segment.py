
def query(node,start,end,left,right):
    global tree
    if right<start or end <left:
        return tree_node()
    if left<=start and end <=right:
        return tree[node]
    mid = (start + end)//2
    p1 = query(2*node,start,mid,left,right)
    p2 = query(2*node+1,mid+1,end,left,right)
    if p1 == p2:
        #print(p1.cha,p1.count+p2.count)
        return tree_node(cha = p1.cha,count = p1.count+p2.count)
    elif p1>p2:
        #print(p1.cha,p1.count)
        return tree_node(cha = p1.cha,count=p1.count)
    else:
        #print(p2.cha,p2.count)
        return tree_node(cha = p2.cha,count = p2.count)

def pn (i):
    print(i.cha,i.count,i.start,i.end)
def pr(tree):
    for j,i in enumerate(tree):
        print(j,i.cha,i.count,i.start,i.end)

class tree_node:
    s = 'abcdefghijklmnopqrstuvwxyz'
    st = {}
    for i,j in enumerate(s):
        st[j]=i
    def __init__(self,cha='a',count=0,start=-1,end=-1):
        self.cha = cha
        self.count = count
        self.start = start
        self.end = end
    def __eq__(self,obj):
        return tree_node.st[self.cha]==tree_node.st[obj.cha]
    def __gt__(self,obj):
        return tree_node.st[self.cha] > tree_node.st[obj.cha]
    def __lt__(self,obj):
        return tree_node.st[self.cha]<tree_node.st[obj.cha]


def build(node,start,end):
    global tree
    global arr
    if start == end:
        tree[node] = tree_node(cha=arr[start],count=1,start=start,end=end)
    else:
        mid = (start +  end)//2
        build(2*node , start , mid)
        build(2*node+1,mid+1,end)

        #left , right = tree[2*node] , tree[2*node+1]
        #if 2*node+2 < len(tree):
        tree[node]=tree_node()
        if tree[2*node] == tree[2*node+1]:
        #if left.cha == right.cha:
            tree[node].cha = tree[2*node].cha
            tree[node].count = tree[2*node].count + tree[2*node+1].count
        elif tree[2*node] > tree[2*node+1]:
            tree[node].cha = tree[2*node].cha
            tree[node].count = tree[2*node].count
        else:
            tree[node].cha = tree[2*node+1].cha
            tree[node].count = tree[2*node+1].count
        tree[node].start = tree[2*node].start
        tree[node].end = tree[2*node+1].end


arr  = "ddaaa"
arr='aaabbcba'
tree = [0]*(len(arr)*2)

#for i in range(1,len(arr)+1):
#    tree[-i] = tree_node(cha = arr[-i],count=1) 
build(1,0,len(arr)-1)

tree[0]=tree_node()
pr(tree)
print('ajfaajljsdflfkjifaeofi')


for i in range(int(input())):
    start = int(input())
    end = int(input())
    q = query(1,0,len(arr)-1,start,end)
    pn(q)

#'''