import  os

filename='book.txt'

def main():
    while True:
        menu()
        choice = int(input("请选择你要使用的功能"))
        if choice in [1, 2, 3, 4, 5]:
            if choice == 5:
                print("谢谢你的使用！")
                break
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()

def menu():
    print('---------------图书管理系统---------------')
    print('-----------------功能菜单----------------')
    print('\t\t\t1.添加图书信息')
    print('\t\t\t2.查找图书信息')
    print('\t\t\t3.删除图书信息')
    print('\t\t\t4.修改图书信息')
    print('\t\t\t5.退出系统')
    print('----------------------------------------')

def insert():
    book_list=[]
    while True:
        id=input('请输入ID:')
        if not id:
            break
        name=input('请输入书名')
        if not name:
            break
        try:
            author=input('请输入作者')
            publishing=input('请输入出版社')
            synopsi=input('请输入简介')
        except:
            print('输入无效')
            continue
        book={'id':id,'name':name,'author':author,'publishing':publishing,'synopsi':synopsi}
        book_list.append(book)
        answer=input('是否继续添加？')
        if answer=="是":
            continue
        else:
            break

    save(book_list)
    print("信息录入完毕")

def save(lst):
    try:
        book_txt=open(filename,'a',encoding='utf-8')
    except:
        book_txt=open(filename,'w',encoding='utf-8')
    for item in lst:
        book_txt.write(str(item)+'\n')
        book_txt.close()

def search():
    book_query=[]
    while True:
        id=''
        name=''
        if os.path.exists(filename):
            mode=input('按ID查找输入1，按书名查找输入2:')
            if mode=='1':
                id=input('请输入图书ID')
            elif mode=='2':
                name=input('请输入图书书名')
            else:
                print('输入有误，请重新输入')
                search()
            with open(filename,'r',encoding='utf-8')as rfile:
                book=rfile.readlines()
                for item in book:
                    d=dict(eval(item))
                    if id!='':
                        if d['id']==id:
                            book_query.append(d)
                    elif name!='':
                       if d['name']==name:
                           book_query.append(d)
            show_book(book_query)
            book_query.clear()
            answer=input("是否要继续查询？")
            if answer=='是':
                continue
            else:
                break
        else:
            print('暂未保存图书信息')
            return

def show_book(lst):
    if len(lst)==0:
        print('没有查询到图书信息')
        return
    format_title='{:^6}\t{:^8}\t{:^10}\t{:^10}\t{:^10}\t'
    print(format_title.format('ID','书名','作者','出版社','简介'))
    format_date='{:^6}\t{:^8}\t{:^10}\t{:^10}\t{:^10}\t'
    for item in lst:
        print(format_date.format(item.get('id'),
                                 item.get('name'),
                                 item.get('author'),
                                 item.get('publishing'),
                                 item.get('synopsi')))

def delete():
    while True:
        book_id=input('请输入要删除的书的ID:')
        if book_id!='':
            if os.path.exists(filename):
                with open(filename,'r',encoding='utf-8')as file:
                    book_old=file.readlines()
            else:
                book_old=[]
            flag=False
            if book_old:
                with open(filename,'w',encoding='utf-8') as wfile:
                    d={}
                    for item in book_old:
                        d=dict(eval(item))
                        if d['id']!=book_id:
                            wfile.write(str(d)+'\n')
                        else:
                            flag=True
                    if flag:
                        print(f'id为{book_id}的书已被删除')
                    else:
                        print(f'没有找到')
            else:
                print('没有找到这本书')
                break
            answer=input('是否继续删除？')
            if answer=='是':
                continue
            else:
               break

def modify():
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8')as rfile:
            book_old=rfile.readlines()
    else:
        return
    book_id=input('请输入要修改图书的ID:')
    with open(filename,'w',encoding='utf-8')as wfile:
        for item in book_old:
            d=dict(eval(item))
            if d['id']==book_id:
                print('找到图书信息，可以修改')
                while True:
                    try:
                        d['name']=input('请输入书名')
                        d['author'] = input('请输入作者')
                        d['publishing'] = input('请输入出版社')
                        d['synopsi'] = input('请输入简介')
                    except:
                        print('输入有误，请重新输入')
                    else:
                        break
                wfile.write(str(d)+'\n')
                print('修改成功')
                break
            else:
                wfile.write(str(d)+'\n')
        answer=input("是否继续修改其它图书信息？")
        if answer=='是':
            modify()

if __name__ == '__main__':
    main()
