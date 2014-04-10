# Read about factories at https://github.com/thoughtbot/factory_girl

FactoryGirl.define do
  factory :community_subtype do
    name "MyString"
    abbr "MyString"
    community_type nil
  end
end
