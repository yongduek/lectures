#include<iostream>
#include <climits>
#include<vector>
using namespace std;
typedef unsigned long long ull;

int bs(int a[], int N, int x) {
    int lb=0, ub=N-1;

    while (lb <= ub) {
        int midx = int( (lb+ub)/2 );
        if (a[midx] == x) {
            return midx;
        }
        else if (a[midx] < x) {
            lb = midx + 1;
        }
        else // x < a[midx] 
        {
            ub = midx - 1;
        }
    }
    return -1; // not found
}

int bs(std::vector<ull>& a, int x) {
	int lb = 0, ub = a.size() - 1;

	while (lb <= ub) {
		int midx = int((lb + ub) / 2);
		if (a[midx] == x) {
			return midx;
		}
		else if (a[midx] < x) {
			lb = midx + 1;
		}
		else // x < a[midx] 
		{
			ub = midx - 1;
		}
	}
	return -1; // not found
}

int bs_recursive(int x, int a[], int N, int lb = -1000, int ub = -1000) {
	if (lb == -1000) lb = 0;
	if (ub == -1000) ub = N - 1;

	if (lb > ub) return -1;

	int midx = int((lb + ub) / 2);
	if (a[midx] == x) {
		return midx;
	}
	else if (a[midx] < x) {
		lb = midx + 1;
		return bs_recursive(x, a, N, lb, ub);
	}
	else // x < a[midx] 
	{
		ub = midx - 1;
		return bs_recursive(x, a, N, lb, ub);
	}
}

/*

int a[500000], b[500000];

int main()
{
    int N, Q;

    cin >> N;
    for (int i = 0; i < N; i++)
        cin >> a[i];

    cin >> Q;
    for (int i = 0; i < Q; i++)
        cin >> b[i];

    for (int i = 0; i < Q; i++) {
        int idx = bs_recursive(b[i], a, N);
        cout << idx << ' ';
    }
}

*/


int main()
{
	int N;
	cin >> N;

	unsigned long long lb = 1, ub = 1ULL<<32;

	while (lb < ub) {
		ull m = (lb + ub) / 2;
		ull m2 = m * m;

		if (m2 == N) {
			lb = m;
			break;
		}
		else if (m2 < N) {
			lb = m;
		}
		else {
			ub = m;
		}

		if ((lb + 1) == ub) break;
	}

	printf("%d\n", lb);
	return 0;
}