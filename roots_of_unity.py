import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

class RootsOfUnity:
    def __init__(self):
        self.n = 5
        self.roots = np.roots( [1,] + [0,]*(self.n-1) + [-1,] )
    def create_view(self):
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('center')
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)

        ax.axes.xaxis.set_ticklabels(["",-1,"","","",1])
        ax.axes.yaxis.set_ticklabels(["","- i","","","","i"])
        # Add arrows to both axes
        ax.plot((1), (0), ls="", marker=">", ms=10, color="k",
                    transform=ax.get_yaxis_transform(), clip_on=False)
        ax.plot((0), (1), ls="", marker="^", ms=10, color="k",
                    transform=ax.get_xaxis_transform(), clip_on=False)

        plt.xlim(-1.5,1.5)
        plt.ylim(-1.5,1.5)
        plt.xticks(fontsize=14, rotation=0)
        plt.yticks(fontsize=14, rotation=0)

        xticks = ax.axes.xaxis.get_major_ticks()
        yticks = ax.axes.yaxis.get_major_ticks()
        yticks[-1].set_visible(False)
        yticks[0].set_visible(False)
        xticks[-1].set_visible(False)
        xticks[0].set_visible(False)


        plt.setp(ax.spines.values(), linewidth=1.5)
        ax.xaxis.set_tick_params(width=1)
        ax.yaxis.set_tick_params(width=1)
        return fig, ax

    def exponent_helper(self, i):
        if(i==4): 
            return 0 
        if(i==2): 
            return 1
        if(i==0):
            return 2 
        if(i==1):
            return 3 
        if(i==3):
            return 4
        return i

    def render(self):
        _, ax = self.create_view()
        circ = plt.Circle((0,0), radius=1, fill=False,
                                color='gray', ls='dashed', lw=.7)
        ax.add_patch(circ)   # make arrows
        i = 0
        for root in self.roots:
            print(root)
            # plt.plot([0,root.real],[0,root.imag],'bo-',label='python')
            plt.plot([root.real], [root.imag], marker='o', markersize=5, color="blue")
            #plt.arrow(0,root.real,0,root.imag, length_includes_head=True, head_width=0.08, head_length=0.00002)
            ax.arrow(0, 0, root.real, root.imag, width=.0000001, head_width=0.0, head_length=0.0,length_includes_head=True, fc='blue', ec='gray')

            plt.text(root.real-0.27, root.imag+.1, "$\omega_%s^%s$" % (str(self.n), self.exponent_helper(i)) , fontsize=14)
            i+= 1
        plt.savefig("preliminary_graphs/roots_of_unity.png",transparent=True)
        plt.show()

r = RootsOfUnity()
r.render()




    




# plt.show()

plt.savefig("unityroots.png",transparent=True)

