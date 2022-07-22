def temp_def():
    case_objs = Case.objects.filter(is_delete=False, is_do=True)
    today = datetime.datetime.now()

    result = defaultdict(int)

    for case in case_objs:
        case_detail_objs = CaseDetail.objects.filter(is_delete=False, is_do=True, case_id=case.case_id)
        for case_detail in case_detail_objs:
            if today < case_detail.start_time_in:
                calculate_week_data(result, case_detail)
            elif case_detail.start_time_in <= today <= case_detail.end_time_in:
                if case_detail.end_time_in.isoweekday() <= 7:
                    # 直接把步骤剩余人日加到本周
                    result[get_monday_friday()] += case_detail.last_person_day_in
                else:
                    # 分周累加，步骤从下周开始的各周剩余的时间到各周
                    case_detail.start_time_in += datetime.timedelta(days=8 - case_detail.start_time_in.isoweekday)
                    calculate_week_data(result, case_detail)
                    # 步骤剩余人日，减去后面几周的各周剩余，结果记为本周人日
                    # calculate_week_data函数里是用的last_person_day_in，外部没办法分，看看是不是可以统一到一起？
            else:  # （today>步骤结束时间）
                # 直接把步骤剩余人日加到本周
                result[get_monday_friday()] += case_detail.last_person_day_in


def temp_def2():
    case_objs = Case.objects.filter(is_delete=False, is_do=True)
    today = datetime.datetime.now()

    result_manpower = defaultdict(int)
    result_case_sources = defaultdict(list)

    for case in case_objs:
        case_detail_objs = CaseDetail.objects.filter(is_delete=False, is_do=True, is_do_in=True,
                                                     case_id=case.case_id)
        for case_detail in case_detail_objs:
            if today <= case_detail.end_time_in:
                calculate_week_data(result_manpower, result_case_sources, case_detail)
            else:  # （today>步骤结束时间）
                # 直接把步骤剩余人日加到本周
                result_manpower[
                    get_monday_friday() + "_" + str(case_detail.work_type_id)] += case_detail.last_person_day_in
                result_case_sources[get_monday_friday() + "_" + str(case_detail.work_type_id)].append(
                    str(case_detail.case_detail_id))
