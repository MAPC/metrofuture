class Region < ActiveRecord::Base
  attr_accessible :abbr, :name, :rpa_name
  has_many :municipalities

  validates :name, presence: true, length: { minimum: 3, maximum: 70 }
  validates :abbr, presence: true, length: { minimum: 3, maximum: 10 }
  validates :rpa_name, presence: true, length: { minimum: 3, maximum: 140 }

end
