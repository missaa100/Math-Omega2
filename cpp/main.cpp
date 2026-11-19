#include <iostream>
#include <string>
#include <cmath>

bool is_prime(long long n) {
    if (n < 2) return false;
    if (n % 2 == 0) return n == 2;
    for (long long d = 3; d <= n / d; d += 2)
        if (n % d == 0) return false;
    return true;
}

int main() {
    std::cout << "MathOmega C++ Compute Core\n";
    std::cout << "Enter an integer (0 to quit): ";
    long long n;
    while (std::cin >> n && n != 0) {
        std::cout << n << (is_prime(n) ? " is prime\n" : " is not prime\n");
        std::cout << "Enter an integer (0 to quit): ";
    }
}
