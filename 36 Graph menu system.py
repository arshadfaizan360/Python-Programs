graph = {
    "Home page": ["Phone info", "Laptop info"],
    "Phone info": ["Phone prices", "Phone service provider"],
    "Phone service provider": ["Phone prices"],
    "Laptop info": ["Laptop prices"],
    "Phone prices": ["Home page"],
    "Laptop prices": ["Home page"]
}

current_option = 1
current_page = "Home page"

while current_option != 0: 
    print('Current page:', current_page)
    print()
    
    print("Menu:")
    for x in graph[current_page]:
        print(str(graph[current_page].index(x) + 1) + ". " + x)
    print("0. Exit")
    print()
    
    while True:
        try:
            current_option = int(input("Choose an option: "))
            if current_option != 0:
                current_page = graph[current_page][current_option-1]
                print()
            break    
        except:
            print('That is not a valid option')
            print()
        