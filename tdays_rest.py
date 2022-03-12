#入力を受け取る部分
sum = int(input())
sum2 = input().split()

#リスト要素をintに変えて再度リストの作成
#宣言
week_sch = []
i = 0

#実行
while i != sum:
	week_sch.append(int(sum2[i]))
	i = i + 1

#作ったリストの中に0が何個あるかを調べる
def check(sch):
	counter = 0
	zeronumber = 0

	while counter != 7:
		if sch[counter] == 0:
			zeronumber = zeronumber + 1
		counter = counter + 1
	
	if(zeronumber < 2):
		return 0
	else:
		return 1

#仕事できる最長の日数をカウントする
def rest_sum(workday):
	workingday = []
	counter_2 = 0
	sum = 0

	while counter_2 != len(workday):
		if workday[counter_2] == 1:
			if sum == 0:
				sum = sum + 7
			else:
				sum = sum + 1
		else:
			if sum == 0:
				sum = 0
			else:
				workingday.append(sum)
				sum = 0
		counter_2 = counter_2 + 1
	if len(workingday) == 0:
		return sum
	else:
		return max(workingday)


#要素数7のリストを作成し、リスト内に0が二個あるかで週休二日制であるかどうかの確認を行う
#宣言
sch_check = [] #7日分の要素をここに入れていく
suc_number = [] #7日分を考えたときに、休みが二日間あるものは1、無いものは0を返すようにしている
i = 0
j = 0
count = 0

while i != sum - 6:
	while(count != 7):
		sch_check.append(week_sch[j])
		j = j + 1
		count = count + 1
	check_rest = check(sch_check)
	suc_number.append(check_rest)
	sch_check = []
	i = i + 1
	j = i
	count = 0

print(rest_sum(suc_number))
