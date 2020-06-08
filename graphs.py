import numpy as np
import matplotlib.pyplot as plt

class Graphs:  
    def create_view(self):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.spines['left'].set_color(self.maincolor)
        ax.spines['bottom'].set_color(self.maincolor)

        ax.spines['bottom'].set_color(self.maincolor)
        ax.spines['left'].set_color(self.maincolor)
        ax.xaxis.label.set_color(self.maincolor)
        ax.yaxis.label.set_color(self.maincolor)
        ax.tick_params(axis='x', colors=self.maincolor)
        ax.tick_params(axis='y', colors=self.maincolor)
        
        plt.xlim(0, 10)
        plt.ylim(0, 10)
        plt.setp(ax.spines.values(), linewidth=1.5)
        
        ax.xaxis.set_tick_params(width=1)
        ax.yaxis.set_tick_params(width=1)
        
        return plt
    def linear_function(self):
        x = np.linspace(0.2,10,100)

        self.maincolor = 'white'
        plt = self.create_view()

        plt.plot(x,x, self.maincolor)
        plt.savefig("introductory_graphs/linear_function.png",transparent=True)
    
    def quadratic_function(self):
        x = np.linspace(0.2,10,100)

        self.maincolor = 'white'
        plt = self.create_view()

        plt.plot(x, x**2, 'w')
        plt.savefig("introductory_graphs/quadratic_function.png",transparent=True)
    
    def cubic_function(self):
        x = np.linspace(0.2,10,100)
        self.maincolor = 'white'
        plt = self.create_view()
        # red dashes, blue squares and green triangles

        plt.plot(x, x**3, 'w')
        plt.savefig("introductory_graphs/cubic_function.png",transparent=True)

    def render_all(self):
        self.linear_function()
        self.quadratic_function()
        self.cubic_function()

g = Graphs()
g.render_all()