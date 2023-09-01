'''
Create Date: 2023/09/01
Author: @1chooo
Version: v0.0.3
'''

import gradio as gr
from Refinaid.Action.Load import get_dataset_x_columns
from Refinaid.gui.Utils.Get import get_data_setting
from Refinaid.Action.ML_configurations import DatasetConfig, DecisionTreeModelConfig, KNNModelConfig

demo = gr.Blocks(
    title='Refinaid',
)

def update_parameters(dataset_name) -> gr.Dropdown:
    parameters = get_dataset_x_columns(dataset_name)

    return gr.Dropdown.update(
            choices=parameters,
            value=[],
            label="Select Mutiple Parameters",
            interactive=True,
        )

def update_plot_x_parameters(dataset_name) -> gr.Dropdown:
    parameters = get_dataset_x_columns(dataset_name)

    return gr.Dropdown.update(
            choices=parameters,
            value=[],
            label="X Axis",
            interactive=True,
        )

def update_plot_y_parameters(dataset_name) -> gr.Dropdown:
    parameters = get_dataset_x_columns(dataset_name)

    return gr.Dropdown.update(
            choices=parameters,
            value=[],
            label="Y Axis",
            interactive=True,
        )

def update_model_parameters(model_name):
    output_components = []
    if model_name == 'Decision Tree Classifier':
        decision_tree_classifer_title = gr.Markdown.update(
            "### Decision Tree Classifier", 
            visible=True,
        )
        decision_tree_classifer_criterion_dropdown = gr.Dropdown.update(
            label="Criterion", 
            choices=[
                "gini", 
                "entropy", 
                "log_loss"
            ], 
            value="gini", 
            interactive=True, 
            visible=True,
        )
        decision_tree_classifer_max_depth_textbox = gr.Textbox.update(
            label="Max Depth", 
            value="None", 
            interactive=True, 
            visible=True,
        )
        decision_tree_classifer_min_samples_split_slider = gr.Slider.update(
            label="Minimum Samples Split", 
            minimum=2, 
            maximum=20, 
            step=1, 
            value=2, 
            interactive=True, 
            visible=True,
        )
        decision_tree_classifer_min_samples_leaf_slider = gr.Slider.update(
            label="Minimum Samples Leaf", 
            minimum=1, 
            maximum=20, 
            step=1, 
            value=1, 
            interactive=True, 
            visible=True,
        )
        decision_tree_classifer_max_features_dropdown = gr.Dropdown.update(
            label="Max Features", 
            choices=[
                "None", 
                "sqrt", 
                "log2"
            ], 
            value="None", 
            interactive=True, 
            visible=True,
        )
        decision_tree_classifer_max_leaf_nodes_textbox = gr.Textbox.update(
            label="Max Leaf Nodes", 
            value="None", 
            interactive=True, 
            visible=True,
        )

        k_neighbors_classifier_title = gr.Markdown.update(
            "### K Neighbors Classifier", 
            visible=False,
        )
        k_neighbors_classifier_slider = gr.Slider.update(
            label="N Neighbors", 
            value=5, 
            interactive=True, 
            minimum=1, 
            maximum=20, 
            step=1, 
            visible=False,
        )
        k_neighbors_classifier_weights_dropdown = gr.Dropdown.update(
            label="Weights", 
            choices=[
                "uniform", 
                "distance"
            ], 
            value="uniform", 
            interactive=True, 
            visible=False,
        )
        k_neighbors_classifier_algorithm_dropdown = gr.Dropdown.update(
            label="Algorithm", 
            choices=[
                "auto", 
                "ball_tree", 
                "kd_tree", 
                "brute"
            ], 
            value="auto", 
            interactive=True, 
            visible=False,
        )
    else:
        output_components = []
        decision_tree_classifer_title = gr.Markdown.update(
            "### Decision Tree Classifier", 
            visible=False,
        )
        decision_tree_classifer_criterion_dropdown = gr.Dropdown.update(
            label="Criterion", 
            choices=[
                "gini", 
                "entropy", 
                "log_loss"
            ], 
            value="gini", 
            interactive=True, 
            visible=False,
        )
        decision_tree_classifer_max_depth_textbox = gr.Textbox.update(
            label="Max Depth", 
            value="None", 
            interactive=True, 
            visible=False,
        )
        decision_tree_classifer_min_samples_split_slider = gr.Slider.update(
            label="Minimum Samples Split", 
            minimum=2, 
            maximum=20, 
            step=1, 
            value=2, 
            interactive=True, 
            visible=False,
        )
        decision_tree_classifer_min_samples_leaf_slider = gr.Slider.update(
            label="Minimum Samples Leaf", 
            minimum=1, 
            maximum=20, 
            step=1, 
            value=1, 
            interactive=True, 
            visible=False,
        )
        decision_tree_classifer_max_features_dropdown = gr.Dropdown.update(
            label="Max Features", 
            choices=[
                "None", 
                "sqrt", 
                "log2"
            ], 
            value="None", 
            interactive=True, 
            visible=False,
        )
        decision_tree_classifer_max_leaf_nodes_textbox = gr.Textbox.update(
            label="Max Leaf Nodes", 
            value="None", 
            interactive=True, 
            visible=False,
        )

        k_neighbors_classifier_title = gr.Markdown.update(
            "### K Neighbors Classifier", 
            visible=True,
        )
        k_neighbors_classifier_slider = gr.Slider.update(
            label="N Neighbors", 
            value=5, 
            interactive=True, 
            minimum=1, 
            maximum=20, 
            step=1, 
            visible=True,
        )
        k_neighbors_classifier_weights_dropdown = gr.Dropdown.update(
            label="Weights", 
            choices=[
                "uniform", 
                "distance"
            ], 
            value="uniform", 
            interactive=True, 
            visible=True,
        )
        k_neighbors_classifier_algorithm_dropdown = gr.Dropdown.update(
            label="Algorithm", 
            choices=[
                "auto", 
                "ball_tree", 
                "kd_tree", 
                "brute"
            ], 
            value="auto", 
            interactive=True, 
            visible=True,
        )


    output_components.append(decision_tree_classifer_title)
    output_components.append(decision_tree_classifer_criterion_dropdown)
    output_components.append(decision_tree_classifer_max_depth_textbox)
    output_components.append(decision_tree_classifer_min_samples_split_slider)
    output_components.append(decision_tree_classifer_min_samples_leaf_slider)
    output_components.append(decision_tree_classifer_max_features_dropdown)
    output_components.append(decision_tree_classifer_max_leaf_nodes_textbox)
    output_components.append(k_neighbors_classifier_title)
    output_components.append(k_neighbors_classifier_slider)
    output_components.append(k_neighbors_classifier_weights_dropdown)
    output_components.append(k_neighbors_classifier_algorithm_dropdown)

    return *output_components,

dataset_choices = [
    "Titanic", 
    "Diabetes", 
    "House Prices",
]

def store_preprocessing_data(
        dataset:str, parameters:list, 
        miss_value:bool, data_scaling:str, 
        training:int, validation:int, testing:int):
    
    model_mapping = {
        "Decision Tree Classifier": "decision_tree_classifier",
        "K Neighbor Classifier": "k_neighbors_classifier",
        "Standard": "standard",
        "Min-Max": "min-max",
        "By Columns": "by_columns",
        "None": None,
        "Drop Nan": None,        
    }

    data_summary_dict = get_data_setting(
        dataset, parameters, miss_value, 
        data_scaling, training, validation, testing
    )
    dataset_config = DatasetConfig(dataset, parameters, model_mapping[miss_value], model_mapping[data_scaling], [training/100, validation/100, testing/100])

with demo:
    our_heading = gr.Markdown("# Simple AI - Bridging the Gap with AI For Everyone")

    with gr.Tab("Preprocessing"):
        our_heading = gr.Markdown("## Preprocessing")
        with gr.Row():
            with gr.Column():
                gr.Markdown("### Dataset")
                dataset_dropdown = gr.Dropdown(
                    label="Select Dataset", 
                    choices=dataset_choices,
                    interactive=True,
                )

                gr.Markdown("### Select Mutiple Parameters")
                parameters_dropdown = gr.Dropdown(
                    label="Select Mutiple Parameters", 
                    choices=[], 
                    interactive=True,
                    multiselect=True,
                )

                gr.Markdown("### Missing Values Handling")
                miss_value_checkbox = gr.Radio(
                    label="Select a Method", 
                    choices=[
                        "Drop Nan", 
                        "By Columns"
                    ], 
                    interactive=True,
                )

                gr.Markdown(f"### Data Split\nTotal value should be 100%")
                data_scale_dd = gr.Radio(
                    choices=[
                        "None", 
                        "Standard", 
                        "Min-Max"
                    ], 
                    label="Please select a method", 
                    interactive=True,
                )
                training_slider = gr.Slider(
                    label="Training Set", 
                    minimum=0, 
                    maximum=100, 
                    step=5,
                    interactive=True,
                )
                validation_slider = gr.Slider(
                    label="Validation Set", 
                    minimum=0, 
                    maximum=100, 
                    step=5,
                    interactive=True,
                )
                testing_slider = gr.Slider(
                    label="Testing Set", 
                    minimum=0, 
                    maximum=100, 
                    step=5,
                    interactive=True,
                )
                submit_dataset_setting_btn = gr.Button(
                    value="Submit Setting",
                )
                
            with gr.Column():
                with gr.Row():
                    gr.ScatterPlot(
                        label="Data Visualization")
                with gr.Row():
                    x_axis_dropdown = gr.Dropdown(
                        label="X Axis", 
                        choices=[], 
                        interactive=True,
                    )
                    y_axis_dropdown = gr.Dropdown(
                        label="Y Axis", 
                        choices=[], 
                        interactive=True,
                    )
        with gr.Row():
            gr.Examples(
                [
                    [
                        "Titanic", 
                        ["PassengerId", "Pclass", "Sex", "Age", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"], 
                        "Drop Nan", 
                        "None", 
                        70, 
                        10, 
                        20
                    ],
                    [
                        "Titanic", 
                        ["PassengerId", "Pclass", "Sex", "Age", "SibSp", "Parch", "Ticket", "Fare"], 
                        "By Columns", 
                        "Standard", 
                        70, 
                        10, 
                        20
                    ],
                    [
                        "Titanic", 
                        ["PassengerId", "Pclass", "Sex", "Age", "SibSp", "Parch", "Ticket", "Fare"], 
                        "By Columns", 
                        "Min-Max", 
                        70, 
                        10, 
                        20
                    ],
                ],
                [
                    dataset_dropdown,
                    parameters_dropdown,
                    miss_value_checkbox, 
                    data_scale_dd, 
                    training_slider, 
                    validation_slider, 
                    testing_slider,
                ]
            )

    with gr.Tab("Training"):
        our_heading = gr.Markdown("## Training")
        with gr.Row():
            with gr.Column():
                gr.Markdown("### Data You have picked!!!")
                gr.DataFrame(
                    headers=[
                        "Parameters",
                        "Value"
                    ],
                    row_count=(7, "fixed"),
                    col_count=(2, "fixed"),
                    interactive=False,
                )
            with gr.Column():
                model_dropdown = gr.Dropdown(
                    label="Select Model", 
                    choices=[
                        "Decision Tree Classifier", 
                        "K Neighbor Classifier",
                    ], 
                    interactive=True
                )
                # Decision Tree Classifier
                decision_tree_classifer_title = gr.Markdown(
                    "### Decision Tree Classifier", 
                    visible=False,
                )
                decision_tree_classifer_criterion_dropdown = gr.Dropdown(
                    label="Criterion", 
                    choices=[
                        "gini", 
                        "entropy", 
                        "log_loss"
                    ], 
                    value="gini", 
                    interactive=True, 
                    visible=False,
                )
                decision_tree_classifer_max_depth_textbox = gr.Textbox(
                    label="Max Depth", 
                    value="None", 
                    interactive=True, 
                    visible=False,
                )
                decision_tree_classifer_min_samples_split_slider = gr.Slider(
                    label="Minimum Samples Split", 
                    minimum=2, 
                    maximum=20, 
                    step=1, 
                    value=2, 
                    interactive=True, 
                    visible=False,
                )
                decision_tree_classifer_min_samples_leaf_slider = gr.Slider(
                    label="Minimum Samples Leaf", 
                    minimum=1, 
                    maximum=20, 
                    step=1, 
                    value=1, 
                    interactive=True, 
                    visible=False,
                )
                decision_tree_classifer_max_features_dropdown = gr.Dropdown(
                    label="Max Features", 
                    choices=[
                        "None", 
                        "sqrt", 
                        "log2"
                    ], 
                    value="None", 
                    interactive=True, 
                    visible=False,
                )
                decision_tree_classifer_max_leaf_nodes_textbox = gr.Textbox(
                    label="Max Leaf Nodes", 
                    value="None", 
                    interactive=True, 
                    visible=False,
                )

                # k_neighbors_classifier
                k_neighbors_classifier_title = gr.Markdown(
                    "### K Neighbors Classifier", 
                    visible=False,
                )
                k_neighbors_classifier_slider = gr.Slider(
                    label="N Neighbors", 
                    value=5, 
                    interactive=True, 
                    minimum=1, 
                    maximum=20, 
                    step=1, 
                    visible=False,
                )
                k_neighbors_classifier_weights_dropdown = gr.Dropdown(
                    label="Weights", 
                    choices=[
                        "uniform", 
                        "distance"
                    ], 
                    value="uniform", 
                    interactive=True, 
                    visible=False,
                )
                k_neighbors_classifier_algorithm_dropdown = gr.Dropdown(
                    label="Algorithm", 
                    choices=[
                        "auto", 
                        "ball_tree", 
                        "kd_tree", 
                        "brute"
                    ], 
                    value="auto", 
                    interactive=True, 
                    visible=False,
                )

        with gr.Row():
            train_btn = gr.Button(
                value="Train"
            )
        with gr.Row():
            gr.Markdown("## Training Result")
        with gr.Row():
            train_df = gr.DataFrame(
                headers=["Accuracy", "Recall", "Precision", "F1"], 
                interactive=True, 
                row_count=(1, "fixed"), 
                col_count=(4, "fixed")
            )

        with gr.Row():
            train_img1 = gr.Plot(
                interactive=True
            )
            train_img2 = gr.Plot(
                interactive=True
            )
            train_img3 = gr.Plot(
                interactive=True
            )

    with gr.Tab("Results"):
        our_heading = gr.Markdown("## Results")
        with gr.Row():
            gr.Textbox("hi")
            gr.Textbox("hi")
        with gr.Row():
            gr.Textbox("hello")
            gr.Textbox("hello")

    dataset_dropdown.change(
        fn=update_parameters,
        inputs=dataset_dropdown,
        outputs=parameters_dropdown,
    )

    dataset_dropdown.change(
        fn=update_plot_x_parameters,
        inputs=dataset_dropdown,
        outputs=x_axis_dropdown,
    )

    dataset_dropdown.change(
        fn=update_plot_y_parameters,
        inputs=dataset_dropdown,
        outputs=y_axis_dropdown,
    )

    model_dropdown.change(
        fn=update_model_parameters,
        inputs=model_dropdown,
        outputs=[
            decision_tree_classifer_title,
            decision_tree_classifer_criterion_dropdown,
            decision_tree_classifer_max_depth_textbox,
            decision_tree_classifer_min_samples_split_slider,
            decision_tree_classifer_min_samples_leaf_slider,
            decision_tree_classifer_max_features_dropdown,
            decision_tree_classifer_max_leaf_nodes_textbox, 
            k_neighbors_classifier_title,
            k_neighbors_classifier_slider,
            k_neighbors_classifier_weights_dropdown,
            k_neighbors_classifier_algorithm_dropdown,
        ]
    )

demo.launch(
    # enable_queue=True,
    # share=True, 
    server_name="127.0.0.1", 
    server_port=6006,
    debug=True,
) 