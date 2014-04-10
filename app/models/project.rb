class Project < ActiveRecord::Base
  attr_accessible :client,
                  :description,
                  :end_date,
                  :equity_comment,
                  :equity_focus,
                  :external_collaborator,
                  :funding_source,
                  :funding_source_id,
                  :start_date,
                  :status,
                  :active,
                  :thumbnail,
                  :thumbnail_file_name,
                  :title,
                  :url,
                  :created_at,
                  :updated_at

  has_and_belongs_to_many :subregions
  has_and_belongs_to_many :municipalities

  has_attached_file :thumbnail
  
  belongs_to :funding_source

  belongs_to :lead_department,    class_name: 'Department', foreign_key: 'lead_department_id'
  belongs_to :partner_department, class_name: 'Department', foreign_key: 'partner_department_id'
  
  validates :title, presence: true, length: { minimum: 3, maximum: 170 }

  # TODO: Can we get rid of "self" throughout these?

  scope :by_lead_department, -> lead_department { where("projects.lead_department ~* ?", name) }
  scope :by_status, -> status { where("projects.status ~* ?", status) }

  def departments
    [self.lead_department, self.partner_department].compact
  end

  def geographies
    self.municipalities + self.subregions
  end

  def display_geographies
    self.municipalities || self.subregions
  end

  def display_geography
    self.display_geographies.first
  end

end