# Parallel Prime Number Checker Using Python Multiprocessing

## Overview

This project demonstrates the implementation of Parallel Computing using Python Multiprocessing.

The program compares sequential execution and parallel execution in finding prime numbers within a specified range. The objective is to evaluate performance improvements achieved through parallel processing and measure the resulting speedup.

## Background

Prime number searching is a computationally intensive task because each number must be checked individually to determine whether it is a prime number.

In sequential execution, all calculations are performed by a single process. In parallel execution, the workload is divided into multiple chunks and processed simultaneously using multiple CPU cores.

## Objectives

- Understand the concept of Parallel Computing
- Implement Multiprocessing in Python
- Compare Sequential and Parallel execution performance
- Measure execution time
- Calculate speedup obtained from parallel processing

## Technologies

- Python 3
- Multiprocessing
- Math Module
- Matplotlib

## Project Features

- Sequential Prime Number Search
- Parallel Prime Number Search
- Execution Time Measurement
- Speedup Calculation
- Performance Visualization

## Experimental Results

| Method | Execution Time (seconds) |
|----------|----------|
| Sequential | 1.5537 |
| Parallel | 0.9973 |

### Prime Numbers Found

41,538 Prime Numbers

### Speedup

Speedup = Sequential Time / Parallel Time

Speedup = 1.5537 / 0.9973

Speedup = 1.56x

## Repository Structure

```text
parallel-prime-checker
│
├── src
│   ├── main.py
│   └── performance_chart.py
│
├── docs
│   ├── index.md
│   ├── introduction.md
│   ├── methodology.md
│   ├── implementation.md
│   ├── results.md
│   └── conclusion.md
│
├── images
│   ├── flowchart.png
│   ├── architecture.png
│   ├── performance.png
|   └── outputcode.png
│
└── README.md
```

## Conclusion

The experiment demonstrates that Python Multiprocessing can improve computational performance by distributing workloads across multiple CPU cores.

The parallel implementation achieved a speedup of 1.56x compared to the sequential implementation.

## Author

**Name:** M. Attiin Mumtaz

**NRP:** 152024051

**Course:** IFB206 Komputasi Paralel

**Institution:** Institut Teknologi Nasional Bandung