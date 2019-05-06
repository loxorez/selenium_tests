from Home12.pages import MainPage


def test_welcome_widget(driver, user_log_in_log_out):
    # Set new welcome widget text and title, save, check changes presence in main page
    main_page = MainPage(driver)
    main_page.open_main_page()
    customize_page = main_page.customize_page_click
    welcome_widget_settings = customize_page.welcome_widget_settings
    input_text = welcome_widget_settings.create_new_content_message
    input_title = welcome_widget_settings.create_new_title_message
    welcome_widget_settings.enable_title()
    customize_page = welcome_widget_settings.save_settings
    main_page = customize_page.finish_customizing
    assert input_text == main_page.custom_widget_text
    assert input_title == main_page.custom_widget_title

