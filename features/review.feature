@wip @review
Feature: Users can get write a review for a product
  Background:
    Given a user opens home page in a browser
    And user selects product(s) to leave a review for using navigation bar and dropdown menus

  @positive
  Scenario: Writing a review for a product
    Given user opens a page with the product(s) to leave a review for
    When user clicks on Review tab
    And user enters his/her name in a corresponding field
    And user types in a text from 25 to 1000 characters long of a review in a corresponding field
    And user rates the product Bad...Good by clicking corresponding radiobutton
    And user clicks Continue button
    Then message "Thank you for your review. It has been submitted to the webmaster for approval" appears