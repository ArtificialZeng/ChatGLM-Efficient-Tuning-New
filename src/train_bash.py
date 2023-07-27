from glmtuner import get_train_args, run_sft, run_rm, run_ppo  # 从 glmtuner 模块导入四个函数：get_train_args、run_sft、run_rm 和 run_ppo

def main():  # 定义主函数
    model_args, data_args, training_args, finetuning_args, general_args = get_train_args()  # 调用 get_train_args() 函数获取关于模型、数据、训练、微调的参数以及一些通用参数

    if general_args.stage == "sft":  # 如果 general_args 中的 stage 参数值为 "sft"
        run_sft(model_args, data_args, training_args, finetuning_args)  # 则执行 run_sft 函数进行自我监督的微调
    elif general_args.stage == "rm":  # 如果 general_args 中的 stage 参数值为 "rm"
        run_rm(model_args, data_args, training_args, finetuning_args)  # 则执行 run_rm 函数进行强化学习
    elif general_args.stage == "ppo":  # 如果 general_args 中的 stage 参数值为 "ppo"
        run_ppo(model_args, data_args, training_args, finetuning_args)  # 则执行 run_ppo 函数进行策略梯度优化

def _mp_fn(index):  # 定义一个名为 _mp_fn 的函数，这个函数接收一个参数 "index"
    # For xla_spawn (TPUs)
    main()  # 这个函数是为了适应使用 XLA（加速线性代数库）进行 TPU（张量处理器）并行处理的情况，调用主函数

if __name__ == "__main__":  # 如果这个脚本被直接运行，而不是作为模块导入
    main()  # 则执行主函数
