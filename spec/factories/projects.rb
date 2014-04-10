# Read about factories at https://github.com/thoughtbot/factory_girl

FactoryGirl.define do
  factory :project do
    title "MyString"
    description "MyText"
    url "MyString"
    thumbnail ""
    external_collaborator "MyString"
    client "MyString"
    funding_id 1
    status "MyString"
    equity_focus false
    equity_comment "MyText"
    start_date "2014-04-09 20:06:05"
    end_date "2014-04-09 20:06:05"
  end
end
