# ChatGLM-Efficient-Tuning-New
ChatGLM-Efficient-Tuning-New-explained


```
├── assets
│   ├── trainer_state.jpg
│   └── wechat.jpg
├── data
│   ├── alpaca_data_en_52k.json
│   ├── alpaca_data_zh_51k.json
│   ├── alpaca_gpt4_data_en.json
│   ├── alpaca_gpt4_data_zh.json
│   ├── belle_multiturn
│   │   └── belle_multiturn.py
│   ├── comparison_gpt4_data_en.json
│   ├── comparison_gpt4_data_zh.json
│   ├── dataset_info.json
│   ├── example_dataset
│   │   ├── example_dataset.py
│   │   └── examples.json
│   ├── hh_rlhf_en
│   │   └── hh_rlhf_en.py
│   ├── oaast_rm.json
│   ├── oaast_rm_zh.json
│   ├── oaast_sft.json
│   ├── oaast_sft_zh.json
│   ├── README.md
│   ├── self_cognition.json
│   └── ultra_chat
│       └── ultra_chat.py
├── examples
│   ├── accelerate_config.yaml
│   ├── ads_generation.md
│   ├── alter_cog_chatglm2.sh
│   ├── alter_self_cognition.md
│   ├── cloudflare-tunnel-to-colab.ipynb
│   ├── covid_doctor.md
│   ├── evaluate.sh
│   ├── media
│   │   ├── ads_generation_1.jpg
│   │   ├── ads_generation_2.jpg
│   │   ├── ads_generation_3.jpg
│   │   ├── ads_generation_4.jpg
│   │   ├── ads_generation_5.jpg
│   │   ├── ads_generation_6.jpg
│   │   ├── alter_self_cognition_1.jpg
│   │   ├── alter_self_cognition_2.jpg
│   │   ├── alter_self_cognition_3.jpg
│   │   ├── covid_doctor_1.jpg
│   │   ├── covid_doctor_2.jpg
│   │   ├── covid_doctor_3.jpg
│   │   ├── covid_doctor_4.jpg
│   │   ├── covid_doctor_5.jpg
│   │   ├── covid_doctor_6.jpg
│   │   ├── covid_doctor_7.jpg
│   │   ├── covid_doctor_8.jpg
│   │   ├── covid_doctor_9.jpg
│   │   └── covid.zip
│   ├── quantized_finetune_with_local_model.sh
│   ├── train_ppo.sh
│   ├── train_rm.sh
│   ├── train_sft_full_tuning.sh
│   ├── train_sft.sh
│   └── train_sft_with_dev_set.sh
├── LICENSE
├── pyproject.toml
├── README.md
├── README_tree.md
├── README_zh.md
├── requirements.txt
├── setup.py
├── src
│   ├── api_demo.py
│   ├── cli_demo.py
│   ├── export_model.py
│   ├── glmtuner
│   │   ├── api
│   │   │   ├── app.py
│   │   │   ├── __init__.py
│   │   │   └── protocol.py
│   │   ├── chat
│   │   │   ├── __init__.py
│   │   │   └── stream_chat.py
│   │   ├── dsets
│   │   │   ├── collator.py
│   │   │   ├── __init__.py
│   │   │   ├── loader.py
│   │   │   └── preprocess.py
│   │   ├── extras
│   │   │   ├── callbacks.py
│   │   │   ├── constants.py
│   │   │   ├── __init__.py
│   │   │   ├── logging.py
│   │   │   ├── misc.py
│   │   │   ├── ploting.py
│   │   │   └── save_and_load.py
│   │   ├── hparams
│   │   │   ├── data_args.py
│   │   │   ├── finetuning_args.py
│   │   │   ├── general_args.py
│   │   │   ├── generating_args.py
│   │   │   ├── __init__.py
│   │   │   └── model_args.py
│   │   ├── __init__.py
│   │   ├── tuner
│   │   │   ├── core
│   │   │   │   ├── adapter.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── loader.py
│   │   │   │   ├── parser.py
│   │   │   │   └── trainer.py
│   │   │   ├── __init__.py
│   │   │   ├── ppo
│   │   │   │   ├── __init__.py
│   │   │   │   ├── trainer.py
│   │   │   │   ├── utils.py
│   │   │   │   └── workflow.py
│   │   │   ├── rm
│   │   │   │   ├── collator.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── metric.py
│   │   │   │   ├── trainer.py
│   │   │   │   └── workflow.py
│   │   │   └── sft
│   │   │       ├── __init__.py
│   │   │       ├── metric.py
│   │   │       ├── trainer.py
│   │   │       └── workflow.py
│   │   └── webui
│   │       ├── chat.py
│   │       ├── common.py
│   │       ├── components
│   │       │   ├── chatbot.py
│   │       │   ├── data.py
│   │       │   ├── eval.py
│   │       │   ├── infer.py
│   │       │   ├── __init__.py
│   │       │   ├── sft.py
│   │       │   └── top.py
│   │       ├── css.py
│   │       ├── __init__.py
│   │       ├── interface.py
│   │       ├── locales.py
│   │       ├── manager.py
│   │       ├── runner.py
│   │       └── utils.py
│   ├── train_bash.py
│   └── train_web.py
├── tests
│   ├── comparison_data_v2.json
│   ├── convert_comparison.py
│   └── translate_hh_rlhf.py
└── tree.md
```
