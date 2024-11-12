# -*- coding: utf-8 -*-
'''
Create Date: 2023/09/02
Author: @1chooo(Hugo ChunHo Lin), @ReeveWu
Version: v0.0.8
'''

from app.utils.update import update_parameters
from app.utils.update import update_plot_x_parameters
from app.utils.update import update_plot_y_parameters
from app.utils.update import update_model_parameters
from app.utils.update import update_preprocessing_data
from app.utils.update import update_training_results
from app.utils.update import update_training_history
from app.utils.update import update_preprocessing_visualization

def background_listener(
        selected_dataset_name,
        select_multiple_parameters_dropdown,
        x_axis_dropdown,
        y_axis_dropdown,
        model_dropdown,
        decision_tree_classifier_title,
        decision_tree_classifier_criterion_dropdown,
        decision_tree_classifier_max_depth_textbox,
        decision_tree_classifier_min_samples_split_slider,
        decision_tree_classifier_min_samples_leaf_slider,
        decision_tree_classifier_max_features_dropdown,
        decision_tree_classifier_max_leaf_nodes_textbox,
        k_neighbors_classifier_title,
        k_neighbors_classifier_slider,
        k_neighbors_classifier_weights_dropdown,
        k_neighbors_classifier_algorithm_dropdown,
        submit_dataset_setting_btn,
        missing_value_checkbox,
        data_scale_dropdown,
        training_slider,
        validation_slider,
        testing_slider,
        preprocessing_data_result,
        train_btn,
        training_results,
        train_img1,
        train_img2,
        train_img3,
        training_history,
        preprocessing_visulize_scatter_plot,
    ) -> None:
        selected_dataset_name.change(
            fn=update_parameters,
            inputs=selected_dataset_name,
            outputs=select_multiple_parameters_dropdown,
        )

        selected_dataset_name.change(
            fn=update_plot_x_parameters,
            inputs=selected_dataset_name,
            outputs=x_axis_dropdown,
        )

        selected_dataset_name.change(
            fn=update_plot_y_parameters,
            inputs=selected_dataset_name,
            outputs=y_axis_dropdown,
        )

        model_dropdown.change(
            fn=update_model_parameters,
            inputs=model_dropdown,
            outputs=[
                decision_tree_classifier_title,
                decision_tree_classifier_criterion_dropdown,
                decision_tree_classifier_max_depth_textbox,
                decision_tree_classifier_min_samples_split_slider,
                decision_tree_classifier_min_samples_leaf_slider,
                decision_tree_classifier_max_features_dropdown,
                decision_tree_classifier_max_leaf_nodes_textbox, 
                k_neighbors_classifier_title,
                k_neighbors_classifier_slider,
                k_neighbors_classifier_weights_dropdown,
                k_neighbors_classifier_algorithm_dropdown,
            ]
        )

        submit_dataset_setting_btn.click(
            fn=update_preprocessing_data, 
            inputs=[
                selected_dataset_name, select_multiple_parameters_dropdown, 
                missing_value_checkbox, data_scale_dropdown, 
                training_slider, validation_slider, testing_slider], 
            outputs=[preprocessing_data_result]
        )

        train_btn.click(
            fn=update_training_results,
            inputs=[
                preprocessing_data_result,
                model_dropdown,
                decision_tree_classifier_criterion_dropdown,
                decision_tree_classifier_max_depth_textbox,
                decision_tree_classifier_min_samples_split_slider,
                decision_tree_classifier_min_samples_leaf_slider,
                decision_tree_classifier_max_features_dropdown,
                decision_tree_classifier_max_leaf_nodes_textbox,
                k_neighbors_classifier_slider,
                k_neighbors_classifier_weights_dropdown,
                k_neighbors_classifier_algorithm_dropdown,
            ],
            outputs=[
                training_results,
                train_img1,
                train_img2,
                train_img3,
            ],
        )

        training_results.change(
            fn=update_training_history,
            inputs=[
                selected_dataset_name,
                model_dropdown,
                training_results,
                training_history,
            ],
            outputs=[
                training_history,
            ],
        )

        x_axis_dropdown.change(
            fn=update_preprocessing_visualization,
            inputs=[
                selected_dataset_name, 
                x_axis_dropdown, 
                y_axis_dropdown,
            ],
            outputs=preprocessing_visulize_scatter_plot
        )

        y_axis_dropdown.change(
            fn=update_preprocessing_visualization,
            inputs=[
                selected_dataset_name, 
                x_axis_dropdown, 
                y_axis_dropdown,
            ],
            outputs=preprocessing_visulize_scatter_plot
        )
        