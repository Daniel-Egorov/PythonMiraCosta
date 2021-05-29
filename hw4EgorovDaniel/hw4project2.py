import graphics as gp
def main():

    window = gp.GraphWin('Sum two numbers', 500, 500)

    title = gp.Text(gp.Point(250, 20), 'I can add two numbers for you!')
    title.draw(window)

    gp.Text(gp.Point(125, 250), '+').draw(window)
    gp.Text(gp.Point(275, 250), '=').draw(window)

    num1input = gp.Entry(gp.Point(50, 250), 5)
    num1input.draw(window)

    num2input = gp.Entry(gp.Point(200, 250), 5)
    num2input.draw(window)

    answerBox = gp.Text(gp.Point(350, 250), '')
    answerBox.draw(window)

    enterButton = gp.Text(gp.Point(250, 300), 'Click here to get your answer')
    enterButton.draw(window)

    window.getMouse()

    num1 = float(num1input.getText())
    num2 = float(num2input.getText())
    answer = num1 + num2

    answerBox.setText(answer)

    enterButton.setText('Click anywhere to quit')

    window.getMouse()
main()