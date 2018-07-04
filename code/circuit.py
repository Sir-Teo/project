import SchemDraw
import SchemDraw.elements as e
class circuit:

    #Constructors
    def __init__(self):
        # a list of lines. The line should be in order
        self.connection = []

    #connect lines in parallel
    def connectInParallel(self, *lines):
        for l in lines:
            self.connection.append(l)

    #connect lines in series
    def connectInSeries(self, *lines):
        for l in lines:
            self.connection.extend(l.elements)

    # There will be more methods to add a new line, or change the order of a line

    # 'ImageName' is the filename of the generated image'
    def evaluate(self, ImageName):
        d = SchemDraw.Drawing()
        d.add(e.LINE, d = 'right')
        #exec(str(self.connection[0]))
        #exec(str(self.connection[1]))
        d.draw()
        d.save(ImageName )
