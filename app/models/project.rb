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


  scope :lead_department, -> lead_department { where("projects.lead_department ~* ?", name) }
  scope :status,          -> status          { where("projects.status ~* ?", status) }

  
  # TODO: Can we get rid of "self" throughout these?

  def departments
    [lead_department, partner_department].compact
  end

  def geographies
    municipalities + subregions
  end

  def display_geographies
    municipalities || subregions
  end

  def display_geography
    display_geographies.first
  end

  def subregion_name
    subregion_names.first if has_subregions? || muni_subregion_name
  end

  def muni_subregion_name
    municipalities.first.subregion_name if has_municipalities?
  end

  # May come in handy later, perhaps.

  def subregion_names
    subregions.pluck(:name) if has_subregions?
  end

  def municipality_names
    municipalities.pluck(:name) if has_municipalities?
  end

  def has_subregions?
    subregions.count > 0
  end

  def has_municipalities?
    municipalities.count > 0
  end




end