class SubStrategy < ActiveRecord::Base
  attr_accessible :title, :letter
  
  belongs_to :strategy

  validates :title,  presence: true, length: { maximum: 140, minimum: 3 }
  validates :letter, presence: true, length: { maximum: 1 }
end