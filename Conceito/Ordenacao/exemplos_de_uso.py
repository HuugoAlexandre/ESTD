from BubbleSort import main as bubble
from SelectionSort import main as selection
from InsertionSort import main as insertion
from ShellSort import main as shell
from MergeSort import main as merge
from QuickSort import main as quick

s1 = [2, 4, 6, 8, 10, 12]
s2 = [11, 9, 7, 5, 3, 1]
s3 = [8, 9, 7, 9, 3, 2, 3, 8, 4, 6]
s4 = [89, 79, 32, 38, 46, 26, 43, 38, 32, 79]

datasets = [s1,s2,s3,s4]

algoritmos = {
    "Bubble Sort" : bubble.bubble_sort,
    "Short Bubble Sort": bubble.short_bubble_sort,
    "Selection Sort": selection.selection_sort,
    "Insertion Sort": insertion.insertion_sort,
    "Shell Sort": shell.shell_sort,
    "Merge Sort": merge.merge_sort,
    "Quick Sort": quick.quick_sort,
}

for nome, funcao in algoritmos.items():
    print(f"### {nome} ###")
    for i, dados in enumerate(datasets, start=1):
        print(f"Resultado para conjunto {i}: {funcao(dados)}")
    print("###################\n")


