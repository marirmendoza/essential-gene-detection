
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

yeast_df = pd.read_csv('results/yeast_final.csv', header=None)
coli_df = pd.read_csv('results/coli_final.csv', header=None)
human_df = pd.read_csv('results/human_final.csv', header=None)
fly_df = pd.read_csv('results/melanogaster_final.csv', header=None)

methods = [
        ['GAT_EXP_SUB_ORT', 'MLP_EXP_SUB_ORT', 'SVM_EXP_SUB_ORT'], 
        [ 'GAT_EXP_ORT', 'MLP_EXP_ORT', 'SVM_EXP_ORT'], 
        ['GAT_EXP_SUB_ORT', 'MLP_EXP_SUB_ORT', 'SVM_EXP_SUB_ORT'], 
        ['GAT_EXP_SUB_ORT', 'MLP_EXP_SUB_ORT', 'SVM_EXP_SUB_ORT'], 
]


plt.style.use('ggplot')
fig = plt.figure(figsize=(10, 8))

# Main plot carrying labels
ax = fig.add_subplot(111)    # The big subplot
ax.set_facecolor('white')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.tick_params(labelcolor='w', top=False, bottom=False, left=False, right=False)

ax.set_ylabel('ROC AUC', labelpad=15)


def plot(ax, df, methods):
    width = 0.6
    labels = ['GAT', 'MLP', 'SVM']

    x = np.arange(len(labels))
    means = np.ones(len(labels))
    for i, method in enumerate(methods):
        mask = (df[0] == method) & (df[2] == 'string')
        means[i] = df[mask][7]

    colors = [c['color'] for c in list(plt.rcParams['axes.prop_cycle'])]
    print(colors)
    rects1 = ax.bar(x, means, width, color=colors[:len(labels)])
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylim(top=1, bottom=0.5)




# Set common labels
#ax.set_xlabel('Organisms')

ax = fig.add_subplot(221)
ax.set_title('Yeast', fontsize=13)
plot(ax, yeast_df, methods[0])

ax = fig.add_subplot(222)
ax.set_title('Coli', fontsize=13)
plot(ax, coli_df, methods[1])

ax = fig.add_subplot(223)
ax.set_title('Human', fontsize=13)
plot(ax, human_df, methods[2])

ax = fig.add_subplot(224)
ax.set_title('Fly', fontsize=13)
plot(ax, fly_df, methods[3])


#fig.subplots_adjust(top=0.90, bottom=0.12, left=0.07, right=1, hspace=0.3)
plt.suptitle('Benchmark of machine learning methods', fontsize=15)
plt.savefig(f'plots/aucs1.pdf')
plt.show()
