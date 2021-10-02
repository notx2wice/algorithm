def solution(fees, records):
    answer = []
    car_id = list()
    car_id_set = set()
    car_fee = dict()
    car_total_time = dict()
    car_stack = dict()
    for x in records:
        a, b, c = map(str, x.split())
        if int(b) in car_id_set:
            continue
        else:
            car_id_set.add(int(b))
            car_id.append(int(b))
    for car in car_id:
        car_fee[car] = 0
        car_stack[car] = []
        car_total_time[car] = 0
    
    car_id.sort()

    for data in records:
        time, car_num, in_out = map(str, data.split())
        time_h , time_m = map(str, time.split(':'))
        car_num = int(car_num)
        ch_to_m = int(time_h) * 60 + int(time_m)
        # print(ch_to_m)
        if len(car_stack[car_num]) == 0:
            car_stack[car_num].append(ch_to_m)
        elif len(car_stack[car_num]) == 1:
            in_time = car_stack[car_num].pop()
            zone_time = ch_to_m - in_time
            car_total_time[car_num] += zone_time

    for car in car_id:
        if len(car_stack[car]) == 1:
            in_time = car_stack[car].pop()
            zone_time = (23 * 60 + 59) - in_time
            car_total_time[car] += zone_time

    # print(car_total_time)

    for car_num in car_id:
        total_t = car_total_time[car_num]
        t_ans = 0
        if total_t <= fees[0]:
            t_ans = fees[1]
        else:
            n_t = total_t - fees[0]
            q = n_t // fees[2]
            p = n_t % fees[2]
            if p == 0:
                t_ans = q * fees[3]
            else:
                t_ans = (q + 1) * fees[3]
            t_ans = t_ans + fees[1]
        answer.append(t_ans)
    
    return answer

if __name__ == "__main__" :
    fees = [180, 5000, 10, 600]
    records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

    print(solution(fees, records) )