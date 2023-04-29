from shapely.geometry import Polygon

def find_all_parallel(A, dot_d):
    Parallel = []
    
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            dot_a = A[i]
            dot_b = A[j]
            vector_a = [dot_a[0] - dot_d[0], dot_a[1] - dot_d[1]]
            dot_c = [round(dot_b[0] + vector_a[0], 6), round(dot_b[1] + vector_a[1], 6)]
            if dot_c in A:
                parallelogram = [dot_a, dot_b, dot_c, dot_d]
                parallelogram = sorted(parallelogram)
                parallelogram[2], parallelogram[3] = parallelogram[3], parallelogram[2]
                Parallel.append(parallelogram)
    return Parallel


def parallelogram_intersection_area(paral1, paral2):
    # Создаем объекты Polygon из заданных координат вершин параллелограммов
    poly1 = Polygon(paral1)
    poly2 = Polygon(paral2)

    # Вычисляем пересечение параллелограммов
    intersection = poly1.intersection(poly2)

    # Если пересечение не является полигоном, возвращаем 0
    if not isinstance(intersection, Polygon):
        return 0

    # Иначе вычисляем площадь пересечения
    return intersection.area


def task_solution(Parallel):
    max_intersection_area = -1
    parallel1 = -1
    parallel2 = -1

    for i in range(len(Parallel)):
        for j in range(i + 1, len(Parallel)):
            # Задаем координаты вершин двух параллелограммов
            parallelogram1 = Parallel[i]
            parallelogram2 = Parallel[j]

            # Вычисляем площадь пересечения двух параллелограммов
            intersection_area = parallelogram_intersection_area(parallelogram1, parallelogram2)

            if intersection_area > max_intersection_area:
                max_intersection_area = intersection_area
                parallel1 = parallelogram1
                parallel2 = parallelogram2

    return max_intersection_area, parallel1, parallel2







