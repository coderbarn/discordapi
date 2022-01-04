#import discord
import matplotlib.pyplot as plt
import numpy as np
#client = discord.Client()

msg = "Hello world"

print(msg)

x = np.linspace(0,20,100) # Create a list of evenly-spaced numbers over the range
plt.plot(x, np.sin(x))
plt.show()