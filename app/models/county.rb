class County < ActiveRecord::Base
  attr_accessible :fips, :name
  has_many :municipalities

  validates :name, presence: true, length: { minimum: 3, maximum: 70 }
end
