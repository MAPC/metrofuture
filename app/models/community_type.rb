class CommunityType < ActiveRecord::Base
  attr_accessible :name, :abbr
  has_many :municipalities

  validates :name, presence: true, length: { maximum: 50, minimum: 3 }
  validates :abbr, presence: true, length: { maximum: 10, minimum: 2 }  
end
