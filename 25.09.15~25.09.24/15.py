# 정수
out_a = '{:d}'.format(52)

# 특정칸에 출력하기
out_b = '{:5d}'.format(52)
out_c = '{:10d}'.format(52)

# 빈칸을 0으로 채우기
out_d = '{:05d}'.format(52)
out_e = '{:05d}'.format(-52)

print("#기본")
print(out_a)
print('#특정 칸에 출력하기')
print(out_b)
print(out_c)
print('#빈칸을 0으로 채우기')
print(out_d)
print(out_e)
