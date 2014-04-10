class Strategy < ActiveRecord::Base
  attr_accessible :number, :title

  has_many :substrategies

  validates :title,  presence: true, length: { maximum: 140, minimum: 3 }
  validates :number, presence: true

end