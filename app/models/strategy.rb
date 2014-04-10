class Strategy < ActiveRecord::Base
  attr_accessible :number, :title

  has_many :sub_strategies

  validates :title,  presence: true, length: { maximum: 140, minimum: 3 }
  validates :number, presence: true

end