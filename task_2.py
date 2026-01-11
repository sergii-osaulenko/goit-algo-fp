import turtle

def draw_pithagoras_tree(t, branch_len, level):
    if level == 0:
        return
    
    t.forward(branch_len)
    
    angle = 45
    t.left(angle)
    draw_pithagoras_tree(t, branch_len * 0.7, level - 1)
    
    t.right(2 * angle)
    draw_pithagoras_tree(t, branch_len * 0.7, level - 1)
    
    t.left(angle)
    t.backward(branch_len)

def main():
    level = int(input("Введіть рівень рекурсії: "))
    
    t = turtle.Turtle()
    t.speed("fastest")
    t.left(90)
    t.up()
    t.goto(0, -200)
    t.down()
    
    draw_pithagoras_tree(t, 100, level)
    turtle.done()

if __name__ == "__main__":
    main()